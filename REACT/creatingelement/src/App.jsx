// RCC Class Based Components
// import React, { Component } from 'react'

// export default class App extends Component {
//   render() {
//     return (
//       <div>App</div>
//     )
//   }
// }
// States in Class Based Components
// Class based components are statefull components
// no need of using react books in class based components since they are statefull components

// RAFC Fucntion based components
// import React from 'react'

// export const App = () => {
//   return (
//     <div>App</div>
//   )
// }

//?useState Hook
//? 1.
// import React, { useState } from 'react'
// export const App = () => {
//     let [state,setState]=useState("hey")
//     let a= ()=>{
//         setState("Hello")
//     }
//   return (
//     <><div>{state}</div>
//     <button onClick={a}>Click</button>
//     </>
//   )
// }


//? 2.
import React, { Component } from 'react'
export default class App extends Component {
    state={
        name:"Sarath",
        age:22
    }
  render() {
    return (
    <>
    <div>{this.state.name}</div>
    <button onClick={()=>{this.setState({name:"Megha"})}}>Click Me</button>
    <button onClick={()=>{this.setState({name:"Sarath"})}}>Return</button>
    </>
    )
  }
}

//PROPS
// properties
// inbuilt object 
// used to transfer the data from parent component to child component
// immutable once vlaue passed from parent component it cannot be changed
// 


