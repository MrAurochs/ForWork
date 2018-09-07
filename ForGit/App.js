import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

var cow = "john remiraz";
var apple = {type:"granny smith"};

var user = {
  location: "new york city",
  name:  "Aaron Silver-Pell",
  age: 176
};

function getLocation(vari){
  if (vari){
    return <p>"Location: " {vari} </p>
  } else {
    return undefined
  }
}

var options = ["option one", "option two"]
var subtitle = "Options"

var template = <div className="App">
<header className="App-header">
  <img src={logo} className="App-logo" alt="logo" />
  <h1 className="App-title">Welcome to React</h1>
  <p>react is a fun way to build todo apps if I can ever get them to work </p>

</header>
<p className="App-intro">
  To get started, edit <code>src/App.js</code> and save to reload.
</p>
<p> the quick brown {cow} jumped over the lazy {apple.type}</p>
{getLocation(user.location)}
<h3> {user.name ? user.name : "Anonymous"}</h3>
<h3>{user.age && user.age >= 18 && <p> Age: {user.age}</p>}</h3> 
<h4> {subtitle && subtitle}</h4>
<p> {options.length > 0 ? "Here are your options" : "you have no options"}</p>
<ol>
  <li> item one </li>
  <li> item two </li>
</ol>
</div>


class App extends Component {
 
  
  render() {
    return (
      template
    );
  }
}

export default App;
