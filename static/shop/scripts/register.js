// Get Elements
const registerForm = document.getElementById('registerForm');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirmPassword');
const registerBtn = document.getElementById('registerBtn');

// SSO Buttons
// const googleSignInBtn = document.getElementById("googleSignInBtn");
// const microsoftSignInBtn = document.getElementById("microsoftSignInBtn");
// const appleSignInBtn = document.getElementById("appleSignInBtn");
// const githubSignInBtn = document.getElementById("githubSignInBtn");

// Error Messages Elements
const emailError = document.getElementById("emailError");
const lengthCheck = document.getElementById("lengthCheck");
const numberCheck = document.getElementById("numberCheck");
const specialCharCheck = document.getElementById("specialCharCheck");
const uppercaseCheck = document.getElementById("uppercaseCheck");
const confirmPasswordCheck = document.getElementById("confirmPasswordCheck");

// const ssoConfig = {
//     google: {
//         clientId: 'YOUR_GOOGLE_CLIENT_ID',
//         scope: 'email profile'
//     },
//     microsoft: {
//         clientId: 'YOUR_MICROSOFT_CLIENT_ID',
//         redirectUri: window.location.origin + '/auth/microsoft/callback',
//         scope: ['user.read', 'email']
//     },
//     apple: {
//         clientId: 'YOUR_APPLE_CLIENT_ID',
//         scope: 'name email',
//         redirectUri: window.location.origin + '/auth/apple/callback'
//     },
//     github: {
//         clientId: 'YOUR_GITHUB_CLIENT_ID',
//         scope: 'user:email',
//         redirectUri: window.location.origin + '/auth/github/callback'
//     }
// };

// Email Validation with strict domain checking
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|edu|net|gov|io)$/;
    return emailRegex.test(email);
}

// Password Validation Criteria
function validatePassword(password) {
    const criteria = {
        length: password.length >= 10,
        number: /\d/.test(password),
        special: /[!@#$%^&*()_+{}|<>?]/.test(password),
        uppercase: /[A-Z]/.test(password)
    };
    return criteria;
}

// Update validation indicators
function updateValidationIndicators(criteria) {
    lengthCheck.innerHTML = criteria.length ? "✅ Minimum 10 characters" : "❌ Minimum 10 characters";
    lengthCheck.style.color = criteria.length ? "green" : "red";

    numberCheck.innerHTML = criteria.number ? "✅ At least 1 number" : "❌ At least 1 number";
    numberCheck.style.color = criteria.number ? "green" : "red";

    specialCharCheck.innerHTML = criteria.special ? "✅ At least 1 special character" : "❌ At least 1 special character";
    specialCharCheck.style.color = criteria.special ? "green" : "red";

    uppercaseCheck.innerHTML = criteria.uppercase ? "✅ At least 1 uppercase letter" : "❌ At least 1 uppercase letter";
    uppercaseCheck.style.color = criteria.uppercase ? "green" : "red";
}

// Show Modal
function showModal(title, message, isError = false) {
    const modalHTML = `
        <div class="modal fade" id="feedbackModal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header ${isError ? 'bg-danger' : 'bg-success'} text-white">
                        <h5 class="modal-title">${title}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <p>${message}</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Remove existing modal if any
    const existingModal = document.getElementById('feedbackModal');
    if (existingModal) {
        existingModal.remove();
    }

    // Add new modal to body
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    // Show the modal
    const modal = new bootstrap.Modal(document.getElementById('feedbackModal'));
    modal.show();

    // Auto-hide after 3 seconds
    setTimeout(() => {
        modal.hide();
    }, 3000);
}

// Initialize SSO Providers
// function initializeSSO() {
//     // Initialize Google Sign-In
//     loadScript('https://apis.google.com/js/platform.js', () => {
//         gapi.load('auth2', () => {
//             gapi.auth2.init({
//                 client_id: ssoConfig.google.clientId,
//                 scope: ssoConfig.google.scope
//             });
//         });
//     });

//     // Initialize Microsoft Authentication
//     loadScript('https://alcdn.msauth.net/browser/2.30.0/js/msal-browser.min.js', () => {
//         const msalConfig = {
//             auth: {
//                 clientId: ssoConfig.microsoft.clientId,
//                 redirectUri: ssoConfig.microsoft.redirectUri
//             }
//         };
//         const msalInstance = new msal.PublicClientApplication(msalConfig);
//         window.msalInstance = msalInstance;
//     });

//     // Initialize Apple Sign-In
//     loadScript('https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js', () => {
//         AppleID.auth.init({
//             clientId: ssoConfig.apple.clientId,
//             scope: ssoConfig.apple.scope,
//             redirectURI: ssoConfig.apple.redirectUri
//         });
//     });

//     // GitHub doesn't require client-side initialization
// }

// Utility function to load external scripts
function loadScript(url, callback) {
    const script = document.createElement('script');
    script.src = url;
    script.onload = callback;
    document.head.appendChild(script);
}

// Handle Google Sign-In
// async function handleGoogleSignIn() {
//     try {
//         const auth2 = gapi.auth2.getAuthInstance();
//         const googleUser = await auth2.signIn();
//         const profile = googleUser.getBasicProfile();

//         return {
//             provider: 'google',
//             id: profile.getId(),
//             name: profile.getName(),
//             email: profile.getEmail(),
//             imageUrl: profile.getImageUrl()
//         };
//     } catch (error) {
//         throw new Error('Google sign-in failed: ' + error.message);
//     }
// }

// Handle Microsoft Sign-In
// async function handleMicrosoftSignIn() {
//     try {
//         const msalInstance = window.msalInstance;
//         const response = await msalInstance.loginPopup({
//             scopes: ssoConfig.microsoft.scope
//         });

//         const graphResponse = await fetch('https://graph.microsoft.com/v1.0/me', {
//             headers: { Authorization: `Bearer ${response.accessToken}` }
//         });
//         const profile = await graphResponse.json();

//         return {
//             provider: 'microsoft',
//             id: profile.id,
//             name: profile.displayName,
//             email: profile.userPrincipalName,
//             imageUrl: null // Microsoft Graph API needs additional permissions for photo
//         };
//     } catch (error) {
//         throw new Error('Microsoft sign-in failed: ' + error.message);
//     }
// }

// Handle Apple Sign-In
// async function handleAppleSignIn() {
//     try {
//         const response = await AppleID.auth.signIn();

//         return {
//             provider: 'apple',
//             id: response.user.id,
//             name: response.user.name?.firstName + ' ' + response.user.name?.lastName,
//             email: response.user.email,
//             imageUrl: null // Apple doesn't provide profile pictures
//         };
//     } catch (error) {
//         throw new Error('Apple sign-in failed: ' + error.message);
//     }
// }

// Handle GitHub Sign-In
// async function handleGithubSignIn() {
//     try {
//         const authUrl = `https://github.com/login/oauth/authorize?client_id=${ssoConfig.github.clientId}&scope=${ssoConfig.github.scope}&redirect_uri=${ssoConfig.github.redirectUri}`;
//         window.location.href = authUrl;
//         // Note: GitHub OAuth flow will continue after redirect
//         // You'll need to handle the callback on your backend
//     } catch (error) {
//         throw new Error('GitHub sign-in failed: ' + error.message);
//     }
// }

// Generic SSO handler
// async function handleSSOSignIn(provider) {
//     try {
//         let userData;

//         switch (provider) {
//             case 'google':
//                 userData = await handleGoogleSignIn();
//                 break;
//             case 'microsoft':
//                 userData = await handleMicrosoftSignIn();
//                 break;
//             case 'apple':
//                 userData = await handleAppleSignIn();
//                 break;
//             case 'github':
//                 await handleGithubSignIn();
//                 return; // GitHub redirects, so we return early
//             default:
//                 throw new Error('Unknown provider');
//         }

//         if (!validateEmail(userData.email)) {
//             showModal("Error", "Please use a valid email domain.", true);
//             return;
//         }

//         showModal("Success", `Welcome ${userData.name}! You've successfully signed in with ${provider}.`);

//         // Store user data or redirect here
//         console.log('SSO User Data:', userData);

//     } catch (error) {
//         showModal("Error", error.message, true);
//         console.error('SSO Error:', error);
//     }
// }

// Email Validation Event Listener
emailInput.addEventListener("input", function() {
    const isValid = validateEmail(this.value);
    emailError.style.display = isValid ? "none" : "block";
    this.classList.toggle('is-invalid', !isValid);
    this.classList.toggle('is-valid', isValid);
});

// Password Validation Event Listener
passwordInput.addEventListener("input", function() {
    const criteria = validatePassword(this.value);
    updateValidationIndicators(criteria);

    // Also update confirm password validation if there's input
    if (confirmPasswordInput.value) {
        const passwordsMatch = this.value === confirmPasswordInput.value;
        confirmPasswordCheck.innerHTML = passwordsMatch ? "✅ Passwords match" : "❌ Passwords do not match";
        confirmPasswordCheck.style.color = passwordsMatch ? "green" : "red";
    }
});

// Confirm Password Event Listener
confirmPasswordInput.addEventListener("input", function() {
    const passwordsMatch = this.value === passwordInput.value;
    confirmPasswordCheck.innerHTML = passwordsMatch ? "✅ Passwords match" : "❌ Passwords do not match";
    confirmPasswordCheck.style.color = passwordsMatch ? "green" : "red";
});

// Form Submission
// registerForm.addEventListener("submit", async function(event) {
//     event.preventDefault();

//     const username = usernameInput.value.trim();
//     const email = emailInput.value.trim();
//     const password = passwordInput.value.trim();
//     const confirmPassword = confirmPasswordInput.value.trim();

//     // Validation checks
//     if (!username || username.length < 3 || username.length > 20) {
//         showModal("Error", "Username must be between 3 and 20 characters.", true);
//         return;
//     }

//     if (!validateEmail(email)) {
//         showModal("Error", "Please enter a valid email address.", true);
//         return;
//     }

//     const passwordCriteria = validatePassword(password);
//     if (!Object.values(passwordCriteria).every(Boolean)) {
//         showModal("Error", "Password does not meet all requirements.", true);
//         return;
//     }

//     if (password !== confirmPassword) {
//         showModal("Error", "Passwords do not match.", true);
//         return;
//     }

//     // If all validations pass, show success message
//     showModal("Success", "Registration successful! Welcome to PCForge!");

//     // Optional: Clear form after successful submission
//     registerForm.reset();
//     updateValidationIndicators({ length: false, number: false, special: false, uppercase: false });
//     emailError.style.display = "none";
//     confirmPasswordCheck.innerHTML = "";
// });

registerForm.addEventListener("submit", async function(event) {
    event.preventDefault(); // Stop default submission temporarily

    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    const confirmPassword = confirmPasswordInput.value.trim();

    // Validation checks
    if (!username || username.length < 3 || username.length > 20) {
        showModal("Error", "Username must be between 3 and 20 characters.", true);
        return;
    }

    if (!validateEmail(email)) {
        showModal("Error", "Please enter a valid email address.", true);
        return;
    }

    const passwordCriteria = validatePassword(password);
    if (!Object.values(passwordCriteria).every(Boolean)) {
        showModal("Error", "Password does not meet all requirements.", true);
        return;
    }

    if (password !== confirmPassword) {
        showModal("Error", "Passwords do not match.", true);
        return;
    }

    // If all validations pass, submit the form manually
    registerForm.submit(); // This sends the form to Django
});

// Add click handlers for SSO buttons
// googleSignInBtn.addEventListener('click', () => handleSSOSignIn('google'));
// microsoftSignInBtn.addEventListener('click', () => handleSSOSignIn('microsoft'));
// appleSignInBtn.addEventListener('click', () => handleSSOSignIn('apple'));
// githubSignInBtn.addEventListener('click', () => handleSSOSignIn('github'));

// Initialize SSO when page loads
// initializeSSO();