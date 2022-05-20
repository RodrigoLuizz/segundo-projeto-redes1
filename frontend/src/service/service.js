import api from './api';

const baseURL = '/';

export default {
  name: 'answerResponsesService',

  async create(data) {
    const body = data;
    return api.post(baseURL, body).then((response) => response.data);
  },

  async update({ id, data }) {
    const body = data

    return api.put(`${baseURL}/${id}`, body).then((respose) => respose.data);
  },

  async delete(id) {
    return api.delete(`${baseURL}/${id}`).then((respose) => respose.data);
  },

  async getById(dataId) {
    return api.get(`${baseURL}/${dataId}`).then((response) => response.data);
  },
};