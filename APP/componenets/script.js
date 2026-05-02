// Password component : Global registered component
Vue.component('password-input',{
  props : ["value"],
  template :`
      <div>
        <p> Give your bank password </p>
        <input type='text' v-model='passwordInput'/>

      </div>
  `,
  data(){
    return {
      passwordInput : this.value,
    };
  },
  watch: {
    passwordInput(newVal){
      this.$emit('input', newVal) // emited to the parent for input
    }
  }
})


// Initiating Vue application
new Vue({
  el : "#app",

  data:{
    password : "Default password",
    strength : 0,
    counter : 0
  },
  methods:{
    HandlePass(){
      console.log(`I am running ${this.counter++} times`);
    }
  }
})

