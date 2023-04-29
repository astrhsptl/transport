import { createAction, createReducer } from "@reduxjs/toolkit";

const initialState = {
    town: {}
}


export default createReducer(
    initialState, 
    {
        [setCurrentTown]: function(state) {
            // console.log(state.count);
            state.town = state.payload 
        },
    })

export const setCurrentTown = createAction('setCurrentTown')
