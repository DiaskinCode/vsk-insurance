import Vue from 'vue';
import {
  ValidationObserver,
  ValidationProvider,
  extend,
  setInteractionMode,
} from 'vee-validate';
import { required, email, length } from 'vee-validate/dist/rules';

setInteractionMode('eager');

// Register it globally
Vue.component('ValidationObserver', ValidationObserver);
Vue.component('ValidationProvider', ValidationProvider);

extend('required', {
  ...required,
  message: 'Обязательное поле'
});

extend('email', {
  ...email,
  message: 'Введите корректный email'
});

extend('length', {
  ...length,
  message: 'Заполните поле полностью'
});

extend('date', {
  validate: (value) => {
    return Date.parse(value.split('.').reverse().join('-'));
  },
  message: 'Введите корректную дату'
});

extend('pastdate', {
  validate: (value) => {
    return Date.parse(value.split('.').reverse().join('-')) < Date.now();
  },
  message: 'Введите корректную дату'
});

extend('containitem', {
  validate: (value) => {
    console.log(value.length)
    return value.length;
  },
  message: 'Обязательное поле'
});

extend('istrue', {
  validate: (value) => {
    return value;
  },
  message: 'Обязательное поле'
});
