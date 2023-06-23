import React from 'react';

export default function SignupForm() {
  return (
    <div>
      <form>
        <div>
        <input
          type='name'
          className='name'
          placeholder="Name"
        />
        <input
          type='text'
          className='email'
          placeholder="Email"
        />
        <input
          type='password'
          className='password'
          placeholder="Password"
        />
        </div>
      </form>
    </div>
  );
}