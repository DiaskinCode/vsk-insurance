<template>
  <transition name="height">
    <div
      v-if="isOpen"
      class="app-menu bg-w d-n d-f-mb fd-c"
    >
      <div class="app-menu__wrapper f-1 px-20 pt-5 pb-40 d-f fd-c jc-sb">
        <AppNav
          class="app-menu__nav"
          :links="links"
          @close="closeMenu"
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
  top: 6.2rem;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1001;
  overflow: hidden;
  max-height: none;

  /* .app-menu__nav */
  &__nav {
    &.app-nav {
      align-items: flex-end;
    }
    .nav-link {
      margin-top: 1rem;
    }
    .nav-link__button {
      margin-top: 1rem;
      font-size: 1.7rem;
    }
    .nav-link__button--primary {
      padding: 1rem 2.5rem;
    }
  }
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
