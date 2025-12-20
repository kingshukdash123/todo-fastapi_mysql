BASE_URL = CONFIG.BASE_URL

// signup 

const signup_form = document.querySelector('.signup-form');
const signup_box = document.querySelector('.signup-box');
const auth_msg = document.querySelector('.auth-err-msg');



auth_msg.style.visibility = 'hidden';


const signup_user = async (data) => {
    try {
        const res = await fetch(`${BASE_URL}/auth/signup/`, {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });


        let returned_data = {}
        try{
            returned_data = await res.json();
        }
        catch(err) {}

        if(!res.ok) {
            auth_msg.style.visibility = 'visible';
            auth_msg.style.color = 'red';
            auth_msg.innerText = returned_data.detail || 'Sign Up failed';
            return false;
        }

        return true;
    }
    catch(err) {
        console.log(err);
        auth_msg.style.visibility = 'visible';
        auth_msg.style.color = 'red';
        auth_msg.innerText = 'Server error. Try again later';

        return false;
    }
}


signup_form.addEventListener('submit', async (e) => {
    e.preventDefault();
    auth_msg.style.visibility = 'hidden';
    
    const name = document.querySelector('#signup-name').value.trim();
    const username = document.querySelector('#signup-username').value.trim();
    const password = document.querySelector('#signup-password').value;
    const re_password = document.querySelector('#signup-re-password').value;
    
    if(password != re_password) {
        auth_msg.style.visibility = 'visible';
        auth_msg.style.color = 'red';
        auth_msg.innerText="Password doesn't match";
        
        return;
    }
    
    show_loader()

    const data = {
        'name': name, 
        'username': username, 
        'password': password,
    }

    const success = await signup_user(data);

    if(success) {
        signup_form.reset();
        window.location.href = 'login.html';
    }

    hide_loader('SIGN UP');
})





// loader

const auth_submit_btn = document.querySelector('.auth-btn')

const show_loader = () => {
    auth_submit_btn.innerText = '';
    auth_submit_btn.disabled = true;
    auth_submit_btn.innerHTML = `<div class="loader"></div>`;
}

const hide_loader = (text) => {
    auth_submit_btn.innerText = text;
    auth_submit_btn.disabled = false;
}