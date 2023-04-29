import React, { useEffect, useState } from 'react'

export default function TransportListRender({busses}) {
  return (
    <>
    {busses?.map((transportList) => 
        <div class="modal__item">
            <div class="item__bus">
                <svg width="20" height="20" viewBox="0 0 84 96" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M49.5 63C49.5 58.875 46.125 55.5 42 55.5C37.6875 55.5 34.5 58.875 34.5 63C34.5 67.3125 37.6875 70.5 42 70.5C46.125 70.5 49.5 67.3125 49.5 63ZM84 20.625C84 8.625 70.6875 0 57.9375 0H25.875C13.3125 0 0 8.625 0 20.625V63.5625C0 72.75 8.0625 80.4375 18.5625 83.0625L7.5 94.125C6.75 94.875 7.3125 96 8.25 96H17.25C18 96 18.5625 95.8125 18.9375 95.4375L30.1875 84H53.625L64.875 95.4375C65.25 95.8125 65.8125 96 66.5625 96H75.5625C76.5 96 77.0625 94.875 76.3125 94.125L65.25 83.0625C75.75 80.4375 84 72.75 84 63.5625V20.625ZM9 42V27H75V42H9ZM9.375 18C11.4375 13.125 18.5625 9 25.875 9H57.9375C65.4375 9 72.5625 13.125 74.4375 18H9.375ZM75 63.5625C75 70.3125 65.0625 75 57.9375 75H25.875C18.5625 75 9 70.3125 9 63.5625V51H75V63.5625Z" fill="#333333"/>
                </svg>
                <div class="item__numbers-bus">
                <div class="number-bus">{transportList.number}</div>
                </div>
            </div>
            <div class="item__rout">
                <div class="rout__stopping">
                <div class="rout__stopping-initial rout__stopping-general">{transportList.stops[0].name}</div>
                <svg width="10" height="10" viewBox="0 0 5 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4.6 3L0.7 5.25167L0.7 0.748334L4.6 3Z" stroke="rgba(24, 142, 252, 1)" stroke-width="0.4"/>
                </svg>
                <div class="rout__stopping-ultimate rout__stopping-general">{transportList.stops[transportList.stops.length-1].name}</div>
                </div>
                <div class="rout__time">Каждый {transportList.periodic.slice(0,5)}</div>
            </div>
            <div class="item__time-block">
                <div class="item__time">{transportList.start_work_time.slice(0, 5)} ⁓ {transportList.end_work_time.slice(0, 5)}</div>
            </div>
        </div>
    )}
    </>
  )
}
