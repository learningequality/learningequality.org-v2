import React, { Component } from 'react';
import PropTypes from 'prop-types';

// Tests that react is working in a new build
export default class TestReact extends Component {
    constructor(props) {
        super(props);

        this.state = {
            greeting: props.greeting,
        };
    }

    render() {
        const { greeting } = this.state;

        const message = `The greeting is ${greeting}`;

        return (
            <div>
                <p className="test">{message}</p>
            </div>
        );
    }
}

TestReact.propTypes = {
    greeting: PropTypes.string.isRequired,
};
