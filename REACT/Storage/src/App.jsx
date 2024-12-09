// import React, { useState } from 'react'
// import Header from './Header';
// const App = () => {
//     let [state,setstate]=useState(0);

//   return (
//     <>
//     <div>{state < 5 && <Header data={{state,setstate}}/>}</div>
//     </>
//   )
// }

// export default App

//! useEffect
// import React, { useEffect } from 'react'

// const App = () => {
//   useEffect(()=>{
//     console.log("useEffect")
//   },[]);
//   console.log("#@$@")
//   return (
//     <div>
//       <ol>
//         <li>Hi</li>
//         <li>Bye</li>
//         <li>Chai</li>
//         <li>Thai</li>
//       </ol>
//     </div>
//   )
// }

// export default App

//! importing component life cycle in Function based components using useEffect
// import React, { useState } from "react";
// import Header from "./Header";

// const App = () => {
//   let [state, setstate] = useState(0);
//   return (
//     <>
//       <Header data={{state,setstate}}/>
//     </>
//   );
// };

// export default App;

//! usEffect - usecase
// import React, { useEffect, useState } from 'react'

// const App = () => {
//   let [state,setstate]=useState("ABC")
//   useEffect(()=>{
//     console.log("Changes are made")
//   },[state])
//   return (
//     <div>
//       <div>{state}</div>
//       <button onClick={()=>{setstate("XYZ")}}>Submit</button>
//     </div>
//   )
// }

// export default App

// ! Counter using useEffect
// import React, { useEffect, useState } from "react";

// const App = () => {
//   let [count, setcount] = useState(0);
//   useEffect(() => {
//     console.log("Counter");
//   }, [count]);
//   return (
//     <div>
//       <div>{count}</div>
//       <button
//         onClick={() => {
//           setcount(count + 1);
//         }}
//       >
//         Click
//       </button>
//     </div>
//   );
// };

// export default App;

// ! Height and Width of Webpage using useEffect
// import React, { useEffect, useState } from "react";

// const App = () => {
//   const [width, setWidth] = useState(window.innerWidth);
//   const [height, setHeight] = useState(window.innerHeight);

//   useEffect(() => {
//     const handleResize = () => {
//       setWidth(window.innerWidth);
//       setHeight(window.innerHeight);
//     };

//     window.addEventListener("resize", handleResize);
//   }, []);

//   return (
//     <div>
//       <div>Width is {width}</div>
//       <div>Height is {height}</div>
//     </div>
//   );
// };

// export default App;
