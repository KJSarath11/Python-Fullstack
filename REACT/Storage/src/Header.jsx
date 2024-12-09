// import React, { Component } from 'react'

// export default class Header extends Component {
//     constructor(){
//         super();
//         this.state={
//             count:0
//         }
//         console.log("constructor")//render only once
//     }
//     componentDidMount(){
//         console.log("didmount")//only once
//     }
//     componentDidUpdate(){
//         console.log("didupdate")//states or props changes then it will change
//     }
//     componentWillUnmount(){
//         console.log("willunmount")//when the condition is satisfied then it will give a message and it will be getting removed
//     }
//   render() {
//     console.log("render")
//     return (
//         <>
//             <h1>{this.props.data.state}</h1>
//             <button onClick={()=>this.props.data.setstate(this.props.data.state+1)}>Clicke Me</button>
//         </>
      
//     )
//   }
// }

//! importing component life cycle in Function based components using useEffect
// import React, { useEffect } from 'react'

// const Header = (a) => {
//     //render method using useEffect 
//     useEffect(()=>{
//         console.log("Render")
//     },[])
//     // component didmount using  useEffect
//     useEffect(()=>{
//         console.log("Didmount")
//     },[])
//      // component didmount using  useEffect
//     useEffect(()=>{
//         console.log("Didupdate")
//     },[])
//      // component didmount using  useEffect
//     useEffect(()=>{
//         console.log("Willunmount")
//     },[])
//   return (
//     <div>{a.data.state}</div>
//   )
// }

// export default Header
