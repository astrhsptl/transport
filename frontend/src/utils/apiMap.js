const server_domain = 'http://v1852484.hosted-by-vdsina.ru/api/v1/docs/';

const apiPaths = {
    register: server_domain + 'auth/login/',
    login: server_domain + 'auth/login/',
    token_pair: server_domain + 'token/',
    token_veify: server_domain + 'token/verify/',
    token_refresh: server_domain + 'token/refresh/',
    townList: server_domain + 'town/',
    transportList: server_domain + 'transport/',
    stopList: server_domain + 'stop/',
    analysisAlertList: server_domain + 'analysis/alert/',
};

export default apiPaths;