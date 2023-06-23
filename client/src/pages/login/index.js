import React, { useState } from 'react';
import LoginForm from '../../components/login-form';
import SignupForm from '../../components/signup-form';

export default function Login() {
  const [isLogin, setIsLogin] = useState(true); // state for rendering login/signup -- default shows login form

  return (
    <div>
      <div className='header'>
        <h1 onClick={() => setIsLogin(true)}>Login</h1>
        <h1 onClick={() => setIsLogin(false)}>Signup</h1>
      </div>
      <div>
        {isLogin ? <LoginForm /> : <SignupForm />}
      </div>
    </div>
  )
}