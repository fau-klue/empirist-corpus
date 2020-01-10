<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="no"/>

  <xsl:variable name="newline">
    <xsl:text>
</xsl:text>
  </xsl:variable>

  <xsl:template match="/">
    <xsl:element name="corpus">
      <xsl:value-of select="$newline"/>
      <xsl:for-each select="corpus/text[@set='test' and @subcorpus='web']">
	<xsl:copy-of select="."/>
	<xsl:value-of select="$newline"/>
      </xsl:for-each>
    </xsl:element>
  </xsl:template>
  
</xsl:stylesheet>
