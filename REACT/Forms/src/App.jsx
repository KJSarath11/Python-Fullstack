//  ?Uncontrolled Form
// import React, { useRef, useState } from "react";

// const App = () => {
//   let num1 = useRef();
//   let num2 = useRef(); //used to target because its function based components
//   let [res, setres] = useState(); //used to change content in the UI

//   let add = (e) => {
//     e.preventDefault();
//     let a = num1x
//     let b = num2

//     setres(parseInt(a) + parseInt(b));
//   };

//   let sub = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) - parseInt(b));
//   };

//   let mul = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) * parseInt(b));
//   };

//   let div = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) / parseInt(b));
//   };
//   return (
//     <>
//       <div>
//         <form action="">
//           <label htmlFor="">Enter your First Number:</label>
//           <input type="number" ref={num1} />
//           <br />
//           <br />
//           <label htmlFor="">Enter your Second Number:</label>
//           <input type="number" ref={num2} />
//           <br />
//           <br />
//           <button type="submit" name="add" onClick={add}>
//             Add
//           </button>
//           &nbsp;&nbsp;
//           <button type="submit" name="sub" onClick={sub}>
//             Sub
//           </button>
//           &nbsp;&nbsp;
//           <button type="submit" name="mul" onClick={mul}>
//             Mul
//           </button>
//           &nbsp;&nbsp;
//           <button type="submit" name="div" onClick={div}>
//             Div
//           </button>
//         </form>
//       </div>
//       <h1>{res}</h1>
//     </>
//   );
// };

// export default App;

//  ?Need to get info/content on UI as well as console concept4
// import React, { useState } from "react";

// const App = () => {
//   let [name, setname] = useState();
//   let [email, setemail] = useState();
//   let [salary, setsalary] = useState();

//   let nameData = (e) => {
//     setname(e.target.value);
//   };
//   let emailData = (e) => {
//     setemail(e.target.value);
//   };
//   let salaryData = (e) => {
//     setsalary(e.target.value);
//   };

//   //to show in the console as an object
//   let formHandle = () => {
//     console.log({ name: name, email: email, salary: salary });
//   };

//   return (
//     <div>
//       <label htmlFor="">Name:</label>
//       <input type="text" value={name} onChange={nameData} />
//       <br />
//       <br />
//       <label htmlFor="">Email:</label>
//       <input type="text" value={email} onChange={emailData} />
//       <br />
//       <br />
//       <label htmlFor="">Salary:</label>
//       <input type="text" value={salary} onChange={salaryData} />
//       <br />
//       <br />
//       <button onClick={formHandle} type="Submit">O/P inside Console</button>
//       <h1>{name}</h1>
//       <h1>{email}</h1>
//       <h1>{salary}</h1>
//     </div>
//   );
// };

// export default App;

//  ?Controlled Form using States concept
// import React, { useRef, useState } from "react";
// import './App.css'

// const App = () => {
//   let [num1, setnum1] = useState();
//   let [num2, setnum2] = useState(); //used to target because its function based components
//   let [res, setres] = useState(); //used to change content in the UI

//   let num1data = (e) => {
//     //function for setnum1
//     setnum1(e.target.value);
//   };
//   let num2data = (e) => {
//     //fucntion for setnum2t
//     setnum2(e.target.value);
//   };

//   let add = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) + parseInt(b));
//   };

//   let sub = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) - parseInt(b));
//   };

//   let mul = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) * parseInt(b));
//   };

//   let div = (e) => {
//     e.preventDefault();
//     let a = num1
//     let b = num2

//     setres(parseInt(a) / parseInt(b));
//   };
//   return (

//       <div>
//         <div id="demo">
//         <form action="">
//           <label htmlFor="">Enter your First Number:</label>
//           <input type="number" value={num1} onChange={num1data} />
//           <br />
//           <br />
//           <label htmlFor="">Enter your Second Number:</label>
//           <input type="number" value={num2} onChange={num2data} />
//           <br />
//           <br />
//           <button type="submit" name="add" onClick={add}>
//             Add
//           </button>
//           &nbsp;&nbsp;
//           <button type="submit" name="sub" onClick={sub}>
//             Sub
//           </button>
//           &nbsp;&nbsp;
//           <button type="submit" name="mu1l" onClick={mul}>
//             Mul
//           </button>
//           &nbsp;&nbsp;
//           <button type="submit" name="div" onClick={div}>
//             Div
//           </button>

//           <h1>Result:&nbsp;{res}</h1>
//         </form>
//         </div>
//       </div>
//   );
// }
// ;

// export default App;
