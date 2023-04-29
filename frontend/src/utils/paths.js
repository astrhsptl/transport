import HomePage from "../pages/HomePage/HomePage";
import AccountPage from "../pages/AccountPage/AccountPage";
import LoginPage from "../pages/LoginPage/LoginPage";
import LogoutPage from "../pages/LogoutPage/LogoutPage";
import RegisterPage from "../pages/RegisterPage/RegisterPage";
import AnalysisPage from "../pages/AnalysisPage/AnalysisPage";
import MretricsPage from "../pages/MetricsPage/MretricsPage";

const paths = [
    {path: '/', component: HomePage, name: 'Home', exact: true,},
    {path: '/register', component: RegisterPage, name: 'Register', exact: true},
    {path: '/login', component: LoginPage, name: 'Login', exact: true},
    {path: '/account', component: AccountPage, name: 'Account', exact: true},
    {path: '/logout', component: LogoutPage, name: 'Logout', exact: true},
    {path: '/analysis', component: AnalysisPage, name: 'Analisys', exact: true},
    {path: '/metrics', component: MretricsPage, name: 'Analisys', exact: true},
  ];

export default paths;