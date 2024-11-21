import React, { useRef, useState } from "react";

const App = () => {
  let num1 = useRef();
  let num2 = useRef(); //used to target because its function based components
  let [res, setres] = useState(); //used to change content in the UI

  let add = (e) => {
    e.preventDefault();
    let a = num1.current.value;
    let b = num2.current.value;

    setres(parseInt(a) + parseInt(b));
  };

  let sub = (e) => {
    e.preventDefault();
    let a = num1.current.value;
    let b = num2.current.value;

    setres(parseInt(a) - parseInt(b));
  };

  let mul = (e) => {
    e.preventDefault();
    let a = num1.current.value;
    let b = num2.current.value;

    setres(parseInt(a) * parseInt(b));
  };

  let div = (e) => {
    e.preventDefault();
    let a = num1.current.value;
    let b = num2.current.value;

    setres(parseInt(a) / parseInt(b));
  };
  return (
    <>
      <div>
        <form action="">
          <label htmlFor="">Enter your First Number:</label>
          <input type="number" ref={num1} />
          <br />
          <br />
          <label htmlFor="">Enter your Second Number:</label>
          <input type="number" ref={num2} />
          <br />
          <br />
          <button type="submit" name="add" onClick={add}>
            Add
          </button>
          &nbsp;&nbsp;
          <button type="submit" name="sub" onClick={sub}>
            Sub
          </button>
          &nbsp;&nbsp;
          <button type="submit" name="mul" onClick={mul}>
            Mul
          </button>
          &nbsp;&nbsp;
          <button type="submit" name="div" onClick={div}>
            Div
          </button>
        </form>
      </div>
      <h1>{res}</h1>
    </>
  );
};

export default App;
