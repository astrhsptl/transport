import { React, useState } from 'react'
import axios from 'axios';
import Header from '../../UI/Header'
import { useNavigate } from "react-router-dom";
import Footer from '../../UI/Footer';

export default function RegisterPage() {
  const navigate = useNavigate();
  let [inputData, setInputData] = useState({
    name: '',
    surname: '',
    username: '',
    email: '',
    password: '',
    itn: '',
  });

  async function APIRequest() {
    inputData.status=1
    inputData.itn = parseInt(inputData.itn)
    let resp = await axios.post("http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/register/", inputData);
    await resp.status === 200 ? Object.keys(resp.data).map( responseParametr => (document.cookie=`${responseParametr}=${resp.data[responseParametr]}`)) : console.log();

    await console.log(document.cookie); 
    return navigate('/account');
  };

  return (
    <div>
      <Header/>
      <div>
      </div>  
      <Footer />
  	</div>
  )
}