<template>
  <button
    class="app-menu-button d-n d-f-mb jc-c ai-c bg-w"
    @click="onClick"
  >
    <div
      class="app-menu-button__icon"
      :class="{ close: isOpen }"
    />
  </button>
</template>

<script>
export default {
  name: 'AppMenuButton',
  props: {
    isOpen: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {
    onClick(event) {
      this.$emit('click', event);
    },
  },

}
</script>

<style lang="scss">
.app-menu-button {
  position: relative;
  width: 3.2rem;
  height: 3.2rem;
  border-radius: .7rem;
  /* .app-menu-button__icon */
  &__icon {
    position: relative;
    width: 2.1rem;
    height: .3rem;
    background-color: $primary;
    border-radius: .4rem;
    transition: all .35s ease;
    &::before,
    &::after{
      top: 0;
      left: 0;
      content: '';
      position: absolute;
      width: 2.1rem;
      height: .3rem;
      background: $primary;
      border-radius: .4rem;
      transition: all .35s ease;
    }
    &::before{
      transform: translateY(-.75rem);
    }
    &::after{
      transform: translateY(.75rem);
    }
    &.close {
      transform: translateX(-50px);
      background: transparent;
      &::before{
        transform: rotate(45deg) translate(35px, -35px);
      }
      &::after{
        transform: rotate(-45deg) translate(35px, 35px);
      }
    }
  }
}
</style>
