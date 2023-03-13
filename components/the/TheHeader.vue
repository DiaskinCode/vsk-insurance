<template>
  <header class="header container-wrapper bb-1 bg-w pos-f">
    <div class="header__content container jc-sb ai-c py-20 py-15-mb">
      <AppLogo
        class="header__logo"
      />
      <AppNav
        class="d-n-mb"
        :links="links"
      />
      <AppMenuButton
        :is-open="isOpen"
        @click="openMenu"
      />
      <AppMenu
        :links="headerLinks"
        :is-open="isOpen"
        @close-menu="openMenu"
      />
    </div>
  </header>
</template>

<script>
export default {
  name: 'TheHeader',
  props: {},
  data: () => ({
    isOpen: false,
    links: [
      {
        href: '#include',
        label: 'Что включает полис',
      },
      {
        href: '#benefit',
        label: 'Преимущества',
      },
      {
        href: '#question',
        label: 'FAQ',
      },
      {
        href: '#calculate',
        label: 'Рассчитать',
        button: true,
      },
    ],
    linksMobile: [
      {
        href: '#include',
        label: 'Что включает полис',
      },
      {
        href: '#benefit',
        label: 'Преимущества',
      },
      {
        href: '#calculate',
        label: 'Калькулятор',
      },
      {
        href: '#question',
        label: 'Ответы на вопросы',
      },
      {
        href: '/logo.svg',
        label: 'Политика в отношении обработки персональных данных',
      },
    ],
  }),
  computed: {
    headerLinks() {
      return this.$mq === 'mb' ? this.linksMobile : this.links;
    },
  },
  methods: {
    openMenu() {
      this.isOpen = !this.isOpen;
      this.setBodyOverflow(this.isOpen);
    },
    setBodyOverflow(hidden) {
      document.body.style.overflow = hidden ? 'hidden' : '';
    },
  },
}
</script>

<style lang="scss">
.header {
  border-color: #F3F3F5;
  z-index: 1001;
  /* .header__logo */
  &__logo {
    margin: -1rem 0;
    @media (max-width: 600px) {
      margin: 0;
    }
  }
}
</style>
