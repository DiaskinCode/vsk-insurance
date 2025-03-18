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
      :class="{ 'left': errorPosition === 'left' }"
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
    },
    errorPosition: {
      type: String,
      default: 'right',
      validator(value) {
        return ['right', 'left'].includes(value);
      },
    },
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
    .app-input, .p-checkbox-box {
      border: 1px solid $error !important;
      box-shadow: 0px 0rem .3rem rgba(255, 0, 0, 0.4) ;
    }
  }
  /* .app-form-field__error */
  &__error {
    bottom: -1.9rem;
    right: 2rem;
    &.left {
      left: 0;
    }
  }
}
</style>
