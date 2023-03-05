<template>
  <ValidationObserver
    ref="observer"
    tag="div"
    class="app-form__wrapper validation-observer"
  >
    <form
      class="app-form d-f fd-c row"
      :class="gyClass"
      autocomplete="off"
      @submit.prevent="submitForm"
    >
      <slot />
    </form>
  </ValidationObserver>
</template>

<script>
export default {
  name: 'AppForm',
  props: {
    gy: {
      type: Number,
      default: 0,
    },
    gx: {
      type: Number,
      default: 0,
    },
  },
  data: () => ({
  }),
  computed: {
    gyClass() {
      return [
        `gy-${this.gy}`,
        `gx-${this.gx}`,
      ];
    },
  },
  methods: {
    submitForm(event) {
      this.$emit('submit', event);
    },
    async validate() {
      const isValid = await this.$refs.observer.validate();
      return isValid;
    },
  },

}
</script>

<style lang="scss">
</style>
