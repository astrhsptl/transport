import React from 'react'

export default function TransportSearchInput({logo, setBusNumber, refetch}) {
    const numberRegexp = /\d+/g;

    return (
    <div class="modal__header">
        <div class="modal__search">
            <div class="search">
                <form onSubmit={(e) => {e.preventDefault()}}>
                    <input 
                        type="text"
                        className="search-field"
                        placeholder="Введите номер транспорта" 
                        onChange={(e) => {
                            e.preventDefault();
                            setBusNumber(Number(e.target.value.match(numberRegexp)?.[0]));
                            refetch();
                        }}
                        />
                </form>
                <img src={logo} alt="#" class="search-icon" />
                <svg width="16" height="16" class="search-icon-2" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="6.5" cy="6.5" r="6" stroke="black"/>
                    <rect x="15.1464" y="15.5732" width="6.67462" height="0.603554" rx="0.301777" transform="rotate(-135 15.1464 15.5732)" stroke="black" stroke-width="0.603554"/>
                </svg>
            </div>
        </div>
    </div>
  )
}
