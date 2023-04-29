import React, { useEffect, useState } from 'react'
import TransportListRender from '../renders/TransportListRender'

export default function TransportListModal({busses}) {
    const [busArray, setbusArray] = useState([]);
    useEffect(()=>{
        setbusArray(busses ? busses : []);
        console.log(busses);
    }, [busses]) ;
  return (
    <main class="main__modal">
        <div class="modal__body">
            <div class="modal__column _container">
                <TransportListRender busses={busses}/>
            </div>
        </div>
    </main>    
  )
}
