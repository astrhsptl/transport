import React, { useEffect, useState } from 'react'
import { Map, Marker, Overlay } from "pigeon-maps";

export default function AlertRender({data}) {
    const [alerts, setAlerts] = useState(data)
  if (alerts?.length > 0) {
    return (
        <>
        {alerts?.map((alert)=> {
            return <Marker
                key={alert.id} 
                width={30} 
                anchor={[alert.lat, alert.lon]}
            />})}
        </>
      )
    }
  else {
    return(
        <>
        </>
    );
  }
}
