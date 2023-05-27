import Vue from 'vue';
import {
  ValidationObserver,
  ValidationProvider,
  extend,
  setInteractionMode,
} from 'vee-validate';
import { required, email, length } from 'vee-validate/dist/rules';
import moment from 'moment';

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
    return moment(value, 'DD.MM.YYYY').isValid();
  },
  message: 'Введите корректную дату'
});

extend('containitem', {
  validate: (value) => {
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

extend('insured-person-min', {
  validate: (value) => {
    return moment(value, 'DD.MM.YYYY').isBefore(moment().subtract(4, 'years'));
  },
  message: 'не моложе 4 лет'
});

extend('insured-person-max', {
  validate: (value) => {
    return moment(value, 'DD.MM.YYYY').isAfter(moment().subtract(70, 'years'));
  },
  message: 'не старше 70 лет'
});

extend('policyholder-min', {
  validate: (value) => {
    return moment(value, 'DD.MM.YYYY').isBefore(moment().subtract(18, 'years'));
  },
  message: 'не моложе 18 лет'
});
