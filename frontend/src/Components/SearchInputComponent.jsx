import axios from 'axios';
import React, { useEffect, useState } from 'react'
import {useSelector, useDispatch} from 'react-redux';
import { useQueries, useQuery } from 'react-query';

import apiPaths from '../utils/apiMap.js';
import logo from '../images/rndsLogo.png';

import '../styles/modalsearch.css';
import '../styles/modaltransport.css';
import TransportSearchInput from './subcomponents/TransportSearchInput.jsx';
import TransportListModal from './subcomponents/TransportListModal.jsx';
import TransportListRender from './renders/TransportListRender.jsx';

async function getTransport(currentTown, inputBusNumber) {
  let data;
  if ((inputBusNumber==NaN || inputBusNumber==undefined) & currentTown.id==undefined) {
    return []
  } 
  else if (inputBusNumber==NaN || inputBusNumber==undefined) {
    data = await axios.get(`${apiPaths.transportList}?town_id=${currentTown.id}`); 

  } else {
    data = await axios.get(`${apiPaths.transportList}?town_id=${currentTown.id}&bus_number=${inputBusNumber}`); 
  }
  return data.data;
};

export default function SearchInputComponent({hidden, currentTown}) {
  const [localHidden, setlocalHidden] = useState(hidden);
  const [inputBusNumber, setInputBusNumber] = useState();

  const {data, isLoading, isError, refetch} = useQuery(
    ['transportList', currentTown, inputBusNumber], 
    () => getTransport(currentTown, inputBusNumber));

  useEffect(()=>{ 
    setlocalHidden(hidden);
  }, [hidden]);

  return (
    <div class="modal__transports" hidden={localHidden}>
      <div class="modal__content">

        <TransportSearchInput 
          logo={logo}
          setBusNumber={setInputBusNumber}
          />
        <TransportListModal 
            busses={data}
        />
      </div>
    </div>
  )
}
