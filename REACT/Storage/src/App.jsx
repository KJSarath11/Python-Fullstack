import React, { useState } from 'react'
import Header from './Header';
const App = () => {
    let [state,setstate]=useState(0);

  return (
    <>
    <div>{state < 5 && <Header data={{state,setstate}}/>}</div>
    </>
  ) 
}

export default App