import Axios from 'axios';


const options =  'http://localhost:8000/';

const api = Axios.create(options);

export default api;