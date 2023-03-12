<template>
  <transition name="height">
    <div
      v-if="isOpen"
      class="app-menu bg-w d-n d-f-mb fd-c"
    >
      <div class="app-menu__wrapper f-1 pt-30 pr-60 pb-40 pl-20 d-f fd-c jc-sb">
        <AppNav
          class="app-menu__nav"
          :links="links"
          @click="closeMenu"
        />
        <div class="">
          <a
            class="fw-6 fs-25 lh-140 c-t15"
            href="tel:8-800-775-15-75"
          >
            8 (800) 775-15-75
          </a>
          <div class="fs-20 mt-5">
            г. Москва, ул. Островная, 4
          </div>
          <div class="d-f mt-20 ai-c">
            <a
              v-for="(link, i) in linksSocial"
              :key="i"
              :class="{'ml-10': i !== 0, [link.class]: true}"
              :href="link.href"
            >
              <img
                :src="link.icon"
                alt="social-link"
              >
            </a>
          </div>
        </div>
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
    linksSocial: [
      {
        href: '#include',
        icon: '/link-icons/yt.svg',
        class: 'footer__link-social--yt',
      },
      {
        href: '#benefit',
        icon: '/link-icons/vk.svg',
        class: 'footer__link-social--vk',
      },
      {
        href: '#calculate',
        icon: '/link-icons/ok.svg',
        class: 'footer__link-social--ok',
      },
    ],
  }),
  computed: {},
  methods: {
    closeMenu() {
      this.$emit('close-menu');
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
      align-items: flex-start;
    }
    .nav-link {
      margin-top: .5rem;
      margin-left: 0;
    }
    .nav-link__button {
      margin-top: 1rem;
      font-size: 1.7rem;
      padding: .5rem;
      .p-button-label {
        text-align: left;
        line-height: 120%;
      }
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
