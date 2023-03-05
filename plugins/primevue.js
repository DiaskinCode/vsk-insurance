import Vue from 'vue';
import PrimeVue from 'primevue/config';

import Button from 'primevue/button';
import Timeline from 'primevue/timeline';
import InputText from 'primevue/inputtext';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
import Slider from 'primevue/slider';
import InputNumber from 'primevue/inputnumber';

import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

Vue.component('Button', Button);
Vue.component('Timeline', Timeline);
Vue.component('InputText', InputText);
Vue.component('Accordion', Accordion);
Vue.component('AccordionTab', AccordionTab);
Vue.component('Slider', Slider);
Vue.component('InputNumber', InputNumber);

Vue.component('Toast', Toast);

Vue.use(ToastService);

Vue.use(PrimeVue, {
  ripple: true
});
