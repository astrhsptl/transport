import { useState } from 'react'
import axios from 'axios';
import { Link, useLocation, useNavigate } from 'react-router-dom'
import Header from '../../UI/Header'
import Footer from '../../UI/Footer';
import apiPaths from '../../utils/apiMap';


export default function LoginPage() {
  let [inputData, setInputData] = useState({
    email: 'root@root.root',
    password: 'root',
  });
  let navigate = useNavigate()
  // async function APIRequest(navigate, inputData) {
  //   let resp = await axios.post("http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/login/", inputData );
  //   await resp.status === 200 ? Object.keys(resp.data).map( responseParametr => (document.cookie=`${responseParametr}=${resp.data[responseParametr]}`)) : console.log();
    
  //   console.log(document.cookie);
  //   return navigate('/account')
  // };


  async function APIRequest(navigate, inputData) {
    let resp = await axios.post(apiPaths.login, {data:{}}, {headers:{'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5NTk3ODY3LCJqdGkiOiI2NTEwYzViNGU5MTQ0Mzc3ODNiMWRiMmUwNzQxODU5YSIsInVzZXJfaWQiOiI1YjUwYTE3MS1jY2RjLTQ5YzgtYTc2My02ZGZjNzRkZDg4NTIifQ.e66OmnfkmuWXJy8AKqBehad9VAXlDkg5jta6q8Ig7E8'}});
    // await resp.status === 200 ? Object.keys(resp.data).map( responseParametr => (document.cookie=`${responseParametr}=${resp.data[responseParametr]}`)) : console.log();
    
    // console.log(document.cookie);
    // return navigate('/account')
    await console.log(resp.data);
  };


  return (
    <div class="wrapper">

      <Header path={useLocation().pathname} />
        <div>
          <button onClick={(e) => {
            e.preventDefault();
            APIRequest(navigate, inputData)

          }}>Send data</button>
        </div>
      <Footer />
  </div>
  )
}
