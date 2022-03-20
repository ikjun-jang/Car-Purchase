import React, { Component } from 'react';
import $ from 'jquery';

import './App.css';
import Purchase from './components/Purchase';

class App extends Component {
  constructor(props){
    super();
    this.state = {
      selectedBattery: 1,
      selectedWheel: 1,
      selectedTire: 1,
      total_price: 0,
      user_name: "",
      total_purchase: 0,
      purchases: [],
    }
  }

  getPurchase = () => {
    $.ajax({
      url: `/report`,
      type: "GET",
      success: (result) => {
        this.setState({
          total_purchase: result.total_purchase,
          purchases: result.purchases
        })
        return;
      }
    })
  }

  purchaseCar = () => {
    if(this.state.user_name != "")
    {
      $.ajax({
        url: '/configure',
        type: "POST",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({
          user_name: this.state.user_name,
          battery: this.state.selectedBattery,
          wheel: this.state.selectedWheel,
          tire: this.state.selectedTire,
        }),
        xhrFields: {
          withCredentials: true
        },
        crossDomain: true,
        success: (result) => {
          alert('Purchase complete! Total price is ' + result.total_price)
          this.getPurchase()
          return;
        },
        error: (error) => {
          alert('Unable to cutomize car. Please try your request again')
          return;
        }
      })
    }
    else
    {
      alert('Please enter user name first')
    }
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }

  componentDidMount(){
    this.getPurchase()
  }

  render() {
    return (
      <div className='App'>
        <h2>Select Options to Purchase Car</h2>
        <h4>
          Battery:&nbsp;
          <select onChange={(e) => {
            this.state.selectedBattery = e.currentTarget.value;
          }}>
            <option value={1}>40kwh</option>
            <option value={2}>60kwh</option>
            <option value={3}>80kwh</option>
          </select>
          &nbsp;&nbsp;Wheel:&nbsp;
          <select onChange={(e) => {
            this.state.selectedWheel = e.currentTarget.value;
          }}>
            <option value={1}>model1</option>
            <option value={2}>model2</option>
            <option value={3}>model3</option>
          </select>
          &nbsp;&nbsp;Tires:&nbsp;
          <select onChange={(e) => {
            this.state.selectedTire = e.currentTarget.value;
          }}>
            <option value={1}>eco</option>
            <option value={2}>performance</option>
            <option value={3}>racing</option>
          </select>
        </h4>
        <h4>
          Enter Name:&nbsp;
          <input type="text" name="user_name" onChange={this.handleChange}/>
          <button name="btn_purchase" onClick={() => {this.purchaseCar()}}>Purchase</button>
        </h4>
        <h3>Purchase List</h3>
        <h4>
          {this.state.purchases.map((purchase) => (
            <Purchase
              key={purchase.id}
              {...purchase}
            />
          ))}
        </h4>
        <h4>
          Total Purchase:&nbsp;{this.state.total_purchase}
        </h4>
      </div>
    );
  }
}

export default App;
