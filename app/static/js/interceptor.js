// Guarda una referencia al `fetch` original
const originalFetch = window.fetch;

async function fetchWithInterceptor(url, options = {}) {
    let accessToken = localStorage.getItem("access_token");

    // Verifica si el token está expirado
    if (accessToken && isTokenExpired(accessToken)) {
        console.log("Access token expired, trying to refresh...");
        accessToken = await refreshAccessToken();

        if (!accessToken) {
            console.error("Could not refresh token. Redirecting to login...");
            alert("Your session has expired. Please log in again.");
            window.location.href = "/";
            throw new Error("Unauthorized");
        }

        // Actualiza los headers con el nuevo token
        options.headers = {
            ...options.headers,
            Authorization: `Bearer ${accessToken}`,
        };
    }

    // Asegúrate de agregar el token a las peticiones
    if (accessToken) {
        options.headers = {
            ...options.headers,
            Authorization: `Bearer ${accessToken}`,
        };
    }

    console.log("options: ", options);
    // Usa el `fetch` original
    const response = await originalFetch(url, options);

    // Si la respuesta es 401, redirige al login
    if (response.status === 401) {
        console.error("Unauthorized request, redirecting to login...");
        alert("Unauthorized request. Redirecting to login...");
        window.location.href = "/";
        throw new Error("Unauthorized");
    }

    // Manejar otros errores
    if (!response.ok) {
        const errorData = await response.json();
        if (errorData.detail) {
            alert(errorData.detail);
        } else {
            alert("An error occurred. Please try again.");
        }
        throw new Error(errorData.detail || "An error occurred");
    }

    return response;
}

// Sobrescribe `window.fetch` con tu interceptor
window.fetch = async (url, options) => {
    return fetchWithInterceptor(url, options);
};

// Función para verificar si el token ha expirado
function isTokenExpired(token) {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.exp < Date.now() / 1000;
}

// Función para refrescar el token de acceso
async function refreshAccessToken() {
    try {
        const response = await originalFetch("/auth/refresh-token", {
            method: "POST",
            credentials: "include",
        });
        if (response.ok) {
            const data = await response.json();
            localStorage.setItem("access_token", data.access_token);
            return data.access_token;
        } else {
            return null;
        }
    } catch (error) {
        console.error("Error refreshing access token:", error);
        return null;
    }
}