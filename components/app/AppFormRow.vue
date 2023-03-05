<template>
  <div class="app-form-row">
    <div
      class="row"
      :class="rowClasses"
    >
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppFormRow',
  props: {
    gy: {
      type: Number,
      default: 0,
    },
    gx: {
      type: Number,
      default: 0,
    },
    innerClass: {
      type: String,
      default: '',
    },
  },
  data: () => ({
  }),
  computed: {
    rowClasses() {
      return [
        `gx-${this.gx}`,
        `gy-${this.gy}`,
        this.innerClass,
      ];
    },
  },
  methods: {
  },
};
</script>

<style lang="scss">
</style>
