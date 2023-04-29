import axios from 'axios';
import React, { useEffect, useState } from 'react'
import {useSelector, useDispatch} from 'react-redux';
import { setCurrentTown } from '../storage/toolkitSlices.js';
import { useQueries, useQuery } from 'react-query';

import logo from '../images/rndsLogo.png';
import apiPaths from '../utils/apiMap.js';

import '../styles/incommon.css' 


async function getTown(town=' ') {
    let {data} = await axios.get(`${apiPaths.townList}?q=${town}`); 
    return data;
  };
  

export default function SelectTownModal({hidden, setIsHidden}) {
    const dispatch = useDispatch();
    const [town, setTown] = useState('')
    const {data, isLoading, isError, refetch} = useQuery(
        ['towns', town], 
        () => getTown(town));

    return (
    <div class="modal__block" hidden={hidden}>
        <div class="modal__body">
            <div class="header__header">
                <div class="header__title">RNDSOFT</div>
            </div>
            <main class="main">
                <div class="main__container _container">
                    <div class="main__title">Выберите город:</div>
                    <form class="main__form" onSubmit={(e)=>{e.preventDefault()}}>
                        <input onChange={(e)=>{
                            setTown(e.target.value);
                            refetch();
                        }} class="main__input" placeholder="Выберите город" />
                        <label class="main__label"><a href="#">
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="6.5" cy="6.5" r="6" stroke="black"/>
                            <rect x="15.1464" y="15.5732" width="6.67462" height="0.603554" rx="0.301777" transform="rotate(-135 15.1464 15.5732)" stroke="black" stroke-width="0.603554"/>
                        </svg>
                        </a></label>
                    </form>
                    <div className='list__town'>
                        {data?.map((town) => 
                        <div 
                            className='item__town'
                            key={town.id}
                            onClick={(e) => {
                                setIsHidden(!Boolean(hidden));
                                dispatch(setCurrentTown(town));
                            }}
                            > {town.name}</div>)}
                    </div>
                    <div class="main__rnd-map">
                        <img src={logo} alt="logo" />
                        <div class="rnd-map__text">map</div>
                    </div>
                </div>
            </main>
            <div class="footer">
            </div>
        </div>
    </div>
  )
}
