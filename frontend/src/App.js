import './App.css';
import React, { useState } from 'react';
import Select from 'react-select'
import axios from 'axios'

function App() {
  const options = [
    { value: 'infix', label: 'Infix'},
    { value: 'prefix', label: 'Prefix'},
    { value: 'postfix', label: 'Postfix'}
  ]

  const [from, setFrom] = useState(options[0])
  const [to, setTo] = useState(options[1])
  const [inputExpression, setInputExpression] = useState('')
  const [outputExpression, setOutputExpression] = useState('')

  function handleFromChange(e) {
    setFrom(e)
  }

  function handleToChange(e) {
    setTo(e)
  }

  function handleInputChange(e) {
    setInputExpression(e.target.value)
  }

  function handleSubmit(e) {
    e.preventDefault();
    axios.post('http://127.0.0.1:5000/solver', {
      initial: from.value,
      final: to.value,
      expression: inputExpression
    })
    .then(function (response) {
      setOutputExpression(response.data)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  return (
    <div className='container'>
      <div className="App">
        <form className='form-element'>
          <div className="headers">
            <h2 className='title'>Expression Form Converter</h2>
            <p className='instructions'>Convert expressions (Infix, Prefix and Postfix) from one type to another!
            Enter the expression and click on 'Convert'! </p>
          </div>
          <div>
            <label className='select-title input-title'>From:</label>
            <Select 
              name='from-options' 
              id='from-options'
              value={from} 
              defaultValue={options[0]}  
              options={options} 
              onChange={handleFromChange}
            />
          </div>

          <div>
            <label className='select-title input-title'>To:</label>
            <Select 
              name='to-options' 
              id='to-options'
              value={to} 
              defaultValue={options[1].value}  
              options={options}
              onChange={handleToChange}
            />
          </div>

          <label className='input-title'>Input Expression:</label>
          <input className='expression' value={inputExpression} onChange={handleInputChange} type='text' placeholder='Enter your expression'/>

          <label className='input-title'>Output:</label>
          <p className='result'>{outputExpression.length > 0 ? outputExpression : 'Enter Input and Convert!'}</p>

          <button className='compute' disabled={!inputExpression} onClick={handleSubmit}>Convert!</button>        
        </form>
      </div>
    </div>
  );
}

export default App;
