import React from 'react'
import Child from './Child'
export const Parent = () => {
  return (
    <>
        <div>Parent</div>
        <div><Child data={
            ["Sarath","Surya","Megha"]
        }/>
        </div>
    </> 
  )
}
export default Parent
