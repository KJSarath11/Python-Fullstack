// import React, { Fragment } from "react";
// import ReactDOM, { createRoot } from "react-dom/client"

// console.log(React)
// console.log(ReactDOM)

//!Native Way
// // let a=React.createElement("p",{id:"demo"},"Hello i am react without JSX",React.createElement("h1",{id:"demo"},"HELLO I AM BUJJI"))
// // createRoot(document.getElementById("root")).render(a)

//!React Way JSX Method
// // let b=<h1>I am Sarath</h1>
// // createRoot(document.getElementById("root")).render(b)

//!React Way JSX Method 2
// // it works for single line Element
// // createRoot(document.getElementById("root")).render(
// // <h1>HII IAM REACT WITH JSX</h1>
// // )

//!it works for Multiple line Element
// createRoot(document.getElementById("root")).render(
//     <Fragment>
//             <h1>HII IAM REACT WITH JSX</h1>
//             <h2>HELLOOO</h2>
//     </Fragment>
// )

// rafc 
import React from 'react';
import ReactDOM from 'react-dom';
import {createRoot} from 'react-dom/client';
import App from './App';

createRoot(document.getElementById("root")).render(<App/>)
