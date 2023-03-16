<template>
  <ValidationProvider
    ref="validationProvider"
    v-slot="{
      errors,
      failed,
    }"
    class="app-form-field d-f fd-c pos-r"
    tag="div"
    :vid="vid"
    :rules="rules"
  >
    <div
      class="app-form-field__content d-f f-1"
      :class="{
        'app-form-field__content--error' : failed,
        'fd-c': labelPositionTop,
      }"
    >
      <label
        v-if="label"
        class="d-b fs-16 fs-15-mb"
        :class="{
          'mb-10': labelPositionTop,
          'mr-10': labelPositionLeft,
        }"
        :for="vid"
      >
        {{ label }}
      </label>
      <slot />
    </div>
    <div
      v-if="failed"
      class="app-form-field__error c-e pos-a fs-14"
    >
      {{ errors[0] }}
    </div>
  </ValidationProvider>
</template>

<script>
export default {
  name: 'AppFormField',
  props: {
    vid: {
      type: String,
      required: true,
    },
    rules: {
      type: String,
      default: '',
    },
    label: {
      type: String,
      default: '',
    },
    labelPosition: {
      type: String,
      default: 'top',
      validator(value) {
        return ['top', 'left'].includes(value);
      },
    }
  },
  data: () => ({
  }),
  computed: {
    labelPositionTop() {
      return this.labelPosition === 'top';
    },
    labelPositionLeft() {
      return this.labelPosition === 'left';
    },
  },
  methods: {
    validate() {
      this.$refs.validationProvider.validate();
    },
    syncValue(val) {
      this.$refs.validationProvider.syncValue(val);
    },
    setErrors(val) {
      this.$refs.validationProvider.setErrors(val);
    },
  },

}
</script>

<style lang="scss">
.app-form-field {
  /* .app-form-field__content--error */
  &__content--error {
    .app-input {
      border: 1px solid $error;
      box-shadow: 0px 0rem .3rem rgba(255, 0, 0, 0.4) ;
    }
  }
  /* .app-form-field__error */
  &__error {
    bottom: -1.9rem;
    right: 2rem;
  }
}
</style>
