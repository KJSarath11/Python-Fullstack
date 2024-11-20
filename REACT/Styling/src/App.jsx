import React from 'react'
import "./App.css"
// we are importing the css file directly

const App = () => {
    let s={color:"red",backgroundColor:"yellow"}
  return (
    <>
    {/* INLINE CSS */}
    {/* <div style={s}>We are </div>
    <h1 style={{color:"white", backgroundColor:"black"}}>Hello Pillaii</h1>
    <h1 style={{color:'yellow',backgroundColor:"red"}}>Hello Pyaaruu</h1> */}

    {/* Global CSS */}
    <div></div>
    <h1>Surya</h1>
    <h2>Megha</h2>
    <h3>Vinaya</h3>
    </>
    
  )
}
export default App
