<template>
  <transition name="height">
    <div
      v-if="isOpen"
      class="app-menu bg-w d-f fd-c"
    >
      <div class="app-menu__wrapper f-1 px-20 pt-20 pb-40 d-f fd-c jc-sb bg-g">
        <AppNav
          mobile
          @close="closeMenu"
        />
        <AppButtonLink
          label="Выбрать пакет"
          href="#packet"
          @click="closeMenu"
        />
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'AppMenu',
  props: {
    isOpen: {
      type: Boolean,
      default: false,
    },
    links: {
      type: Array,
      required: true,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {
    closeMenu() {
      this.$emit('close');
    },
  },

}
</script>

<style lang="scss">
.app-menu {
  position: fixed;
  top: 7.2rem;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1001;
  overflow: hidden;
  max-height: none;
}

.height-enter-active,
.height-leave-active {
  transition: all .5s ease;
}

.height-enter-active.height-enter,
.height-leave-active.height-leave-to {
  bottom: 100%;
}
</style>
