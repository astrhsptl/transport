import axios from 'axios';
import React, { useEffect, useRef, useState } from 'react'
import { Link } from "react-router-dom";
import { Map, Marker, Overlay } from "pigeon-maps";
import {useSelector, useDispatch } from 'react-redux';
import { useQueries, useQuery } from 'react-query';
import SearchInputComponent from '../../Components/SearchInputComponent';
import SelectTownModal from '../../Components/SelectTownModal';

import '../../styles/map.css';
import apiPaths from '../../utils/apiMap.js';

async function getTown(currentTown) {
  if (currentTown.id === undefined){
    return []
  };
  let {data} = await axios.get(`${apiPaths.stopList}?town_id=${currentTown.id}`); 
  await console.log(data)
  return data;
};

export default function HomePage() {
  const [location, setLocation] = useState();
  const [modalHiddenDependences, setModalHiddenDependences] = useState(false)
  const currentTown = useSelector(state => state.toolkit.town);
  const {data, isLoading, isError, refetch} = useQuery(
    ['stops', currentTown], 
    () => getTown(currentTown));

  useEffect(()=>{
    setLocation(navigator.geolocation.getCurrentPosition((position)=>{setLocation(position.coords)}, (error)=>{console.log(error)}));
  }, [])

  return (
    <>
      <Link to={'/analysis'}><div className='button__analysis'>Анализ</div></Link>
      <SearchInputComponent 
        hidden={Boolean(!modalHiddenDependences)}
        currentTown={currentTown}/>  
      <SelectTownModal 
        hidden={modalHiddenDependences} 
        setIsHidden={setModalHiddenDependences}/>
      <Map 
        boxClassname='map__background' 
        defaultCenter={location ? [location?.latitude, location?.longitude] : [55.4507, 37.3656]} 
        center={[location?.latitude, location?.longitude]}
        defaultZoom={15}>
          { 
          data?.map((stops)=> {
            return <Overlay 
                    key={stops.id} 
                    width={30} 
                    anchor={[stops.lat, stops.lon]}
                    offset={[stops.lat, stops.lon]}>
                      <svg width="19" height="21" viewBox="0 0 19 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect width="19" height="21" fill="#188EFC"/>
                        <path d="M10.7656 13.1562C10.7656 12.4258 10.168 11.8281 9.4375 11.8281C8.67383 11.8281 8.10938 12.4258 8.10938 13.1562C8.10938 13.9199 8.67383 14.4844 9.4375 14.4844C10.168 14.4844 10.7656 13.9199 10.7656 13.1562ZM16.875 5.65234C16.875 3.52734 14.5176 2 12.2598 2H6.58203C4.35742 2 2 3.52734 2 5.65234V13.2559C2 14.8828 3.42773 16.2441 5.28711 16.709L3.32812 18.668C3.19531 18.8008 3.29492 19 3.46094 19H5.05469C5.1875 19 5.28711 18.9668 5.35352 18.9004L7.3457 16.875H11.4961L13.4883 18.9004C13.5547 18.9668 13.6543 19 13.7871 19H15.3809C15.5469 19 15.6465 18.8008 15.5137 18.668L13.5547 16.709C15.4141 16.2441 16.875 14.8828 16.875 13.2559V5.65234ZM3.59375 9.4375V6.78125H15.2812V9.4375H3.59375ZM3.66016 5.1875C4.02539 4.32422 5.28711 3.59375 6.58203 3.59375H12.2598C13.5879 3.59375 14.8496 4.32422 15.1816 5.1875H3.66016ZM15.2812 13.2559C15.2812 14.4512 13.5215 15.2812 12.2598 15.2812H6.58203C5.28711 15.2812 3.59375 14.4512 3.59375 13.2559V11.0312H15.2812V13.2559Z" fill="white"/>
                      </svg></Overlay>})}
      </Map>
    </>
);};

      {/* <YMaps>
        <Map 
           defaultState={{ center: [location?.latitude, location?.longitude], zoom: 11 }}
          width={'100%'}
          height={'100vh'}>
            {/* <Placemark geometry={ [location?.latitude, location?.longitude] } /> 
        </Map>
      </YMaps> */}
            {/* <MapContainer center={position} zoom={13} scrollWheelZoom={false}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
        <Marker position={position}>
          <Popup>
            A pretty CSS3 popup. <br /> Easily customizable.
          </Popup>
        </Marker>
      </MapContainer> */}