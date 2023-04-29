import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate, Navigate, Link } from 'react-router-dom';
import Header from '../../UI/Header';
import getCookies from '../../utils/cookies';
import Footer from '../../UI/Footer';


export default function AccountPage() {
    const [user, setUser] = useState(getCookies());
    const [staff, setStaff] = useState([]);
    const [statuses, setStatuses] = useState([]);
    const [changes, setChanges] = useState([]);
    const navigator = useNavigate();

    useEffect(() => {
        async function getData(setStat, setChanges, setStaff, id){
            let statuses = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/status/');
            let asd = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/change/make/?manager=${id}`);        
            let staff = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/users/');
    
            await setStaff(staff.data)
            await setChanges(asd.data);
            await setStat(statuses.data);
        }
        getData(setStatuses, setChanges, setStaff, user.id)
    }, [])

    return (
        <div className='wrapper__home'>
            <Header />
            <div></div>
            <Footer />
        </div>
    )
}