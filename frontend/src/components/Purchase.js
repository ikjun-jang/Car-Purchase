import React, { Component } from 'react';

export default class Purchase extends Component {
    render() {
        let {id, user_name, battery, wheel, tire, price} = this.props;

        return (
            <div name="Purchase">
                <span name="user_name">Name: {user_name} </span>
                <span name="battery">Battery: {battery} </span>
                <span name="wheel">Wheel: {wheel} </span>
                <span name="tire">Tires: {tire} </span>
                <span name="total_price">Total Price: {price}</span>
            </div>
        );
    }
}