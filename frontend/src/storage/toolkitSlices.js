import { createSlice } from "@reduxjs/toolkit";

const townSlice = createSlice({
    name: 'toolkit',
    initialState: {
        town: {},
    },
    
    reducers: {
        setCurrentTown(state, town) {
            state.town=town.payload;
        },
    }
});

export default townSlice.reducer
export const {setCurrentTown} = townSlice.actions;