<template>
  <div class="login-page">
    <div class="login-card">
      <div class="d-flex justify-content-center">Senha eletrônica</div>
      <div class="pt-3">
        <i class="bi bi-shield-lock" style="font-size: 20px"></i
        ><input
          type="password"
          class="email password_action formStyle"
          id="user_password"
          name="user_password"
          required
        />
      </div>
      <div class="pt-5 row d-flex justify-content-center">
        <div class="col-3 card" @click="moveNumbers(1)">0 ou 4</div>
        <div class="col-3 card" @click="moveNumbers(2)">1 ou 5</div>
        <div class="col-3 card" @click="moveNumbers(3)">2 ou 6</div>
        <div class="col-3 card" @click="moveNumbers(4)">3 ou 8</div>
        <div class="col-3 card" @click="moveNumbers(4)">7 ou 9</div>
        <div class="col-3 card">
          <i class="bi bi-backspace" @click="removeNumber()"></i>
        </div>
      </div>
      <div class="d-flex justify-content-center">
        <button type="button" class="mt-4 button-primary">acessar</button>
      </div>
      <div class="mt-4 d-flex justify-content-center">
        <div class="forgot">esqueci minha senha</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      data: [],
    };
  },
  methods: {
    moveNumbers(id) {
      const num = id;
      var txt = document.getElementById('user_password').value;
      txt = txt + num;
      document.getElementById('user_password').value = txt;
      this.data.push(id)
      console.log(this.data);
    },
    removeNumber() {
      var txt = document.getElementById('user_password').value;
      document.getElementById('user_password').value = txt.substring(
        0,
        txt.length - 1
      );
      this.data.splice(-1)
    },
  },
};
</script>
<style>
.login-page {
  background-image: url('../../public/img/backgroundImg.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.login-card {
  background-color: rgba(0, 0, 0, 0.281);
  text-align: center;

  padding: 40px;
  color: white;
}
.button-primary {
  color: grey;
  background: white;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  border-radius: 4px;
  height: 40px;
  display: flex;
  width: 44.375644994840044vh;
}
.button-primary:hover {
  transition: 0.3s;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 5px 8px;
}
.formStyle {
  background-color: rgba(0, 0, 0, 0);
  color: white;
  border: none;
  width: 250px;
  border-bottom: 2px solid white;
  transition: all 0.3s ease-in-out 0s;
  outline: none !important;
}
.card {
  color: grey;
  font-weight: bold;
  margin: 10px;
  padding: 8px;
  width: 70px;
  border-radius: 4px;
  cursor: pointer;
}
.forgot {
  cursor: pointer;
}
.forgot:hover {
  text-decoration: underline;
}
</style>
