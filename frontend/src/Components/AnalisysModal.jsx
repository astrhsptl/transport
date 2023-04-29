import axios from 'axios';
import React, { useEffect, useState } from 'react'
import {useSelector, useDispatch} from 'react-redux';
import { useQueries, useQuery } from 'react-query';

import apiPaths from '../utils/apiMap.js';
import logo from '../images/rndsLogo.png';
import DateTimePicker from 'react-datetime-picker';
import '../styles/modalsearch.css';
import '../styles/modalanalisys.css';
import TransportSearchInput from './subcomponents/TransportSearchInput.jsx';

import 'react-datetime-picker/dist/DateTimePicker.css';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';

export default function AnalisysModal({setInputBusNumber, refetch, value, onChange}) {  
    return (
      <div class="modal__analisys">
        <div class="modal__content">
  
          <TransportSearchInput 
            logo={logo}
            setBusNumber={setInputBusNumber}
            refetch={refetch}
            />
            <DateTimePicker onChange={onChange} value={value} />
        </div>
      </div>
    )
  }