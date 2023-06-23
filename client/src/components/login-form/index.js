import React from "react";

export default function LoginForm() {
  return (
    <div>
    <form>
      <div>
        <input
          type='text'
          id='email'
          placeholder="Email"
        >
        </input>
        <input
          type='password'
          id='password'
          placeholder="Password"
        >
        </input>
      </div>
    </form>
  </div>
  )
}