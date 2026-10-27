import React, { useState } from "react";
import "./Register.css";

const Register = () => {
    const [userName, setUserName] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    const gohome = () => {
        window.location.href = "/";
    };

    const register = async (e) => {
        e.preventDefault();
        setError("");

        try {
            const registerUrl =
                window.location.origin + "/djangoapp/register";

            const response = await fetch(registerUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    userName,
                    firstName,
                    lastName,
                    email,
                    password,
                }),
            });

            const json = await response.json();

            if (
                response.ok &&
                json.status === "Authenticated"
            ) {
                sessionStorage.setItem(
                    "username",
                    json.userName
                );

                window.location.href = "/";
            } else if (json.error === "Already Registered") {
                setError(
                    "This username is already registered. Please choose another."
                );
            } else {
                setError(
                    json.error || "Registration failed."
                );
            }
        } catch (err) {
            setError(
                "Unable to contact the server. Please try again."
            );
        }
    };

    return (
        <div
            className="register_container"
            style={{ width: "50%" }}
        >
            <div
                className="header"
                style={{
                    display: "flex",
                    flexDirection: "row",
                    justifyContent: "space-between",
                    fontSize: "2.5rem",
                }}
            >
                <span className="text">Sign Up</span>

                <button
                    type="button"
                    onClick={gohome}
                    aria-label="Close registration"
                    style={{
                        border: "none",
                        background: "transparent",
                        cursor: "pointer",
                        fontSize: "2rem",
                    }}
                >
                    ×
                </button>
            </div>

            <form onSubmit={register}>
                <div className="inputs">

                    <div className="input">
                        <input
                            type="text"
                            name="username"
                            placeholder="Username"
                            aria-label="Username"
                            className="input_field"
                            value={userName}
                            onChange={(e) =>
                                setUserName(e.target.value)
                            }
                            autoComplete="username"
                            required
                        />
                    </div>

                    <div className="input">
                        <input
                            type="text"
                            name="firstName"
                            placeholder="First Name"
                            aria-label="First Name"
                            className="input_field"
                            value={firstName}
                            onChange={(e) =>
                                setFirstName(e.target.value)
                            }
                            autoComplete="given-name"
                            required
                        />
                    </div>

                    <div className="input">
                        <input
                            type="text"
                            name="lastName"
                            placeholder="Last Name"
                            aria-label="Last Name"
                            className="input_field"
                            value={lastName}
                            onChange={(e) =>
                                setLastName(e.target.value)
                            }
                            autoComplete="family-name"
                            required
                        />
                    </div>

                    <div className="input">
                        <input
                            type="email"
                            name="email"
                            placeholder="Email"
                            aria-label="Email"
                            className="input_field"
                            value={email}
                            onChange={(e) =>
                                setEmail(e.target.value)
                            }
                            autoComplete="email"
                            required
                        />
                    </div>

                    <div className="input">
                        <input
                            type="password"
                            name="password"
                            placeholder="Password"
                            aria-label="Password"
                            className="input_field"
                            value={password}
                            onChange={(e) =>
                                setPassword(e.target.value)
                            }
                            autoComplete="new-password"
                            required
                        />
                    </div>

                </div>

                {error && (
                    <p
                        role="alert"
                        style={{
                            color: "darkred",
                            textAlign: "center",
                            padding: "0 12px",
                        }}
                    >
                        {error}
                    </p>
                )}

                <div className="submit_panel">
                    <input
                        className="submit"
                        type="submit"
                        value="Register"
                    />
                </div>
            </form>
        </div>
    );
};

export default Register;
