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

    // Usa el `fetch` original
    const response = await originalFetch(url, options);

    // Si la respuesta es 401, redirige al login
    if (response.status === 401) {
        console.error("Unauthorized request, redirecting to login...");
        window.location.href = "/";
        throw new Error("Unauthorized");
    }

    return response;
}

// Sobrescribe `window.fetch` con tu interceptor
window.fetch = async (url, options) => {
    return fetchWithInterceptor(url, options);
};
